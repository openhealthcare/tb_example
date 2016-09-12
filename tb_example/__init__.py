"""
tb_example - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    flow_module   = 'tb_example.flow'
    javascripts   = [
        'js/tb_example/routes.js',
        'js/tb_example/add_patient_step.js',
        'js/tb_example/add_contact_step.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/tb_example/flow.js',
    ]
