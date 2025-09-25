import ast
import operator
from typing import Any, Dict, Optional

class PolicyConditionEvaluator:
    """Safe condition evaluator with whitelisted operations"""
    
    # Allowed operations
    ALLOWED_OPERATORS = {
        ast.And: lambda values: all(values),
        ast.Or: lambda values: any(values),
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.In: lambda x, y: x in y,
        ast.NotIn: lambda x, y: x not in y,
    }
    
    # Allowed node types
    ALLOWED_NODES = {
        ast.Expression,
        ast.BoolOp,
        ast.Compare,
        ast.Name,
        ast.Attribute,
        ast.Constant,
        ast.List,
    }
    
    def __init__(self):
        self.context = {}
    
    def eval_condition(self, expr: str, user: Dict[str, Any], record: Optional[Dict[str, Any]] = None, ctx: Optional[Dict[str, Any]] = None) -> bool:
        """
        Evaluate a condition expression safely
        
        Args:
            expr: Condition expression string
            user: User claims dictionary
            record: Record data dictionary
            ctx: Additional context dictionary
            
        Returns:
            Boolean result of condition evaluation
        """
        if not expr or not expr.strip():
            return True
        
        try:
            # Build context
            self.context = {
                'user': user,
                'record': record or {},
                'ctx': ctx or {},
            }
            
            # Parse and evaluate
            tree = ast.parse(expr, mode='eval')
            return self._eval_node(tree.body)
            
        except Exception as e:
            # Log error and default to False for security
            print(f"Policy condition evaluation error: {e}")
            return False
    
    def _eval_node(self, node: ast.AST) -> Any:
        """Recursively evaluate AST nodes"""
        if type(node) not in self.ALLOWED_NODES:
            raise ValueError(f"Node type {type(node)} not allowed")
        
        if isinstance(node, ast.Expression):
            return self._eval_node(node.body)
        
        elif isinstance(node, ast.Constant):
            return node.value
        
        elif isinstance(node, ast.List):
            return [self._eval_node(elt) for elt in node.elts]
        
        elif isinstance(node, ast.Name):
            return self._get_variable(node.id)
        
        elif isinstance(node, ast.Attribute):
            # Handle attribute access like user.roles
            value = self._eval_node(node.value)
            if hasattr(value, node.attr):
                return getattr(value, node.attr)
            elif isinstance(value, dict) and node.attr in value:
                return value[node.attr]
            else:
                return None
        
        elif isinstance(node, ast.BoolOp):
            op = self.ALLOWED_OPERATORS.get(type(node.op))
            if not op:
                raise ValueError(f"Operator {type(node.op)} not allowed")
            
            values = [self._eval_node(v) for v in node.values]
            return op(values)
        
        elif isinstance(node, ast.Compare):
            if len(node.ops) != 1 or len(node.comparators) != 1:
                raise ValueError("Only single comparisons allowed")
            
            left = self._eval_node(node.left)
            right = self._eval_node(node.comparators[0])
            op = self.ALLOWED_OPERATORS.get(type(node.ops[0]))
            
            if not op:
                raise ValueError(f"Comparison operator {type(node.ops[0])} not allowed")
            
            return op(left, right)
        
        else:
            raise ValueError(f"Unsupported node type: {type(node)}")
    
    def _get_variable(self, name: str) -> Any:
        """Get variable value from context using dot notation"""
        parts = name.split('.')
        value = self.context
        
        try:
            for part in parts:
                if isinstance(value, dict):
                    value = value[part]
                else:
                    value = getattr(value, part)
            return value
        except (KeyError, AttributeError):
            return None

# Global instance
evaluator = PolicyConditionEvaluator()

def eval_condition(expr: str, user: Dict[str, Any], record: Optional[Dict[str, Any]] = None, ctx: Optional[Dict[str, Any]] = None) -> bool:
    """Convenience function for condition evaluation"""
    return evaluator.eval_condition(expr, user, record, ctx)
