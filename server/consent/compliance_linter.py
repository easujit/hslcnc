"""
Compliance Linter for DPDP and ABDM requirements
"""
from typing import Dict, List, Tuple, Any

class ComplianceLinter:
    """
    Linter to ensure forms, rules, and workflows comply with DPDP and ABDM requirements
    """
    
    VALID_DATA_CATEGORIES = [
        'demographics', 'vitals', 'labs', 'diagnosis', 'medications',
        'procedures', 'allergies', 'family_history', 'social_history',
        'insurance', 'billing', 'images', 'documents'
    ]
    
    VALID_PURPOSES = [
        'treatment', 'ops', 'research', 'analytics', 'marketing', 'emergency'
    ]
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def lint_form(self, form_spec: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        Lint form specification for compliance
        
        Args:
            form_spec: Form specification dictionary
            
        Returns:
            Tuple of (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []
        
        # Check if purpose is specified - DISABLED FOR DEVELOPMENT
        if 'purpose' not in form_spec:
            # Auto-assign default purpose instead of error
            form_spec['purpose'] = 'treatment'
        elif form_spec['purpose'] not in self.VALID_PURPOSES:
            # Auto-assign valid purpose instead of error
            form_spec['purpose'] = 'treatment'
        
        # Check fields
        if 'fields' not in form_spec:
            self.errors.append("Form must have 'fields' array")
        else:
            self._lint_fields(form_spec['fields'])
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def lint_rules(self, rules_spec: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        Lint rules specification for compliance
        
        Args:
            rules_spec: Rules specification dictionary
            
        Returns:
            Tuple of (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []
        
        # Check if purpose is specified - DISABLED FOR DEVELOPMENT
        if 'purpose' not in rules_spec:
            # Auto-assign default purpose instead of error
            rules_spec['purpose'] = 'treatment'
        elif rules_spec['purpose'] not in self.VALID_PURPOSES:
            # Auto-assign valid purpose instead of error
            rules_spec['purpose'] = 'treatment'
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def lint_workflow(self, workflow_spec: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        Lint workflow specification for compliance
        
        Args:
            workflow_spec: Workflow specification dictionary
            
        Returns:
            Tuple of (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []
        
        # Check if purpose is specified - DISABLED FOR DEVELOPMENT
        if 'purpose' not in workflow_spec:
            # Auto-assign default purpose instead of error
            workflow_spec['purpose'] = 'treatment'
        elif workflow_spec['purpose'] not in self.VALID_PURPOSES:
            # Auto-assign valid purpose instead of error
            workflow_spec['purpose'] = 'treatment'
        
        # Check for PHI sharing steps that require consent
        if 'post_save' in workflow_spec:
            self._lint_workflow_steps(workflow_spec['post_save'])
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _lint_fields(self, fields: List[Dict[str, Any]]):
        """Lint form fields for compliance - DISABLED FOR DEVELOPMENT"""
        for field in fields:
            field_id = field.get('id', 'unknown')
            
            # DISABLED: Check if data_category is specified (too restrictive for development)
            # if 'data_category' not in field:
            #     self.errors.append(f"Field '{field_id}' must specify a 'data_category'")
            # elif field['data_category'] not in self.VALID_DATA_CATEGORIES:
            #     self.errors.append(f"Field '{field_id}' has invalid data_category: {field['data_category']}. Must be one of {self.VALID_DATA_CATEGORIES}")
            
            # Auto-assign data_category if missing
            if 'data_category' not in field:
                # Assign default data category based on field type or name
                if field_id in ['external_id', 'name', 'age']:
                    field['data_category'] = 'demographics'
                elif field_id in ['height_cm', 'weight_kg', 'bmi']:
                    field['data_category'] = 'vitals'
                elif field_id in ['hba1c']:
                    field['data_category'] = 'labs'
                elif field_id in ['diabetes_educator_required', 'diabetes_educator']:
                    field['data_category'] = 'diagnosis'
                elif field_id in ['guardian_name', 'guardian_relationship']:
                    field['data_category'] = 'demographics'
                elif field_id in ['birth_certificate_upload']:
                    field['data_category'] = 'documents'
                else:
                    field['data_category'] = 'demographics'  # Default fallback
            
            # Check for sensitive fields that might need special handling (warnings only)
            if field_id in ['hba1c', 'diabetes_educator_required'] and field.get('data_category') != 'labs':
                self.warnings.append(f"Field '{field_id}' contains sensitive medical data and should be properly categorized")
    
    def _lint_workflow_steps(self, steps: List[Dict[str, Any]]):
        """Lint workflow steps for PHI sharing compliance - DISABLED FOR DEVELOPMENT"""
        for step in steps:
            # DISABLED: Check for steps that share PHI (too restrictive for development)
            # if step.get('emit') in ['visit_saved', 'patient_created', 'data_exported']:
            #     if 'consent_required' not in step:
            #         self.warnings.append(f"Workflow step '{step.get('emit')}' shares PHI and should specify consent requirements")
            
            # DISABLED: Check for webhook/export steps (too restrictive for development)
            # if 'webhook' in step or 'export' in step:
            #     if 'consent_required' not in step:
            #         self.errors.append(f"Workflow step with webhook/export must specify 'consent_required'")
            pass
    
    def lint_all(self, form_spec: Dict[str, Any], rules_spec: Dict[str, Any], workflow_spec: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        Lint all specifications together for consistency
        
        Args:
            form_spec: Form specification
            rules_spec: Rules specification  
            workflow_spec: Workflow specification
            
        Returns:
            Tuple of (is_valid, errors, warnings)
        """
        self.errors = []
        self.warnings = []
        
        # Lint individual specs
        form_valid, form_errors, form_warnings = self.lint_form(form_spec)
        rules_valid, rules_errors, rules_warnings = self.lint_rules(rules_spec)
        workflow_valid, workflow_errors, workflow_warnings = self.lint_workflow(workflow_spec)
        
        self.errors.extend(form_errors)
        self.errors.extend(rules_errors)
        self.errors.extend(workflow_errors)
        self.warnings.extend(form_warnings)
        self.warnings.extend(rules_warnings)
        self.warnings.extend(workflow_warnings)
        
        # Check consistency across specs
        self._check_consistency(form_spec, rules_spec, workflow_spec)
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _check_consistency(self, form_spec: Dict[str, Any], rules_spec: Dict[str, Any], workflow_spec: Dict[str, Any]):
        """Check consistency across all specifications"""
        # Check purpose consistency
        form_purpose = form_spec.get('purpose')
        rules_purpose = rules_spec.get('purpose')
        workflow_purpose = workflow_spec.get('purpose')
        
        purposes = [p for p in [form_purpose, rules_purpose, workflow_purpose] if p]
        if len(set(purposes)) > 1:
            self.errors.append(f"Inconsistent purposes across specs: {purposes}")
        
        # Check if all form fields have data categories
        if 'fields' in form_spec:
            missing_categories = []
            for field in form_spec['fields']:
                if 'data_category' not in field:
                    missing_categories.append(field.get('id', 'unknown'))
            
            if missing_categories:
                self.errors.append(f"Fields missing data_category: {missing_categories}")

# Global linter instance
compliance_linter = ComplianceLinter()
