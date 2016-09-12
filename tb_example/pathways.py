from pathway import pathways
from tb_example import models
from opal.models import Patient


class ExamplePathway(object):
    def save(self, *args, **kwargs):
        patient = Patient.objects.create()
        patient.create_episode()
        return patient

    def redirect_url(self, patient):
        return "/#/"


class AddPatient(ExamplePathway, pathways.Pathway):
    display_name = "Add Patient"
    slug = "add_patient"
    icon = "fa fa-user-md"

    steps = (
        pathways.Step(
            model=models.Location,
            template_url="/templates/pathway/add_patient.html",
            controller_class="AddPatient"
        ),
    )


class ContactScreening(ExamplePathway, pathways.Pathway,):
    display_name = "Add Contact"
    slug = "add_contact"
    icon = "fa fa-user-md"

    steps = (
        pathways.Step(
            model=models.Location,
            template_url="/templates/pathway/add_contact.html",
            controller_class="AddContact"
        ),
    )
