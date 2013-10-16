import logging; logger = logging.getLogger("minimalKB."+__name__);
DEBUG_LEVEL=logging.DEBUG

class TemplateBackend:

    def __init__(self):

    def clear(self):
        """ Empties all knowledge models.
        """
        raise NotImplementedError()

    def add(self, stmts, model = "default"):
        """ Add the given statements to the given model.
        """
        raise NotImplementedError()

    def delete(self, stmts, model = "default"):
        """ remove the given statements from the given model.
        """
        raise NotImplementedError()

    def update(self, stmts, model = "default"):
        """ Add the given statements to the given model, updating the statements
        with a functional predicate.
        """
        raise NotImplementedError()

    def about(self, resource, models):
        """ Returns all statements involving the resource.
        """
        raise NotImplementedError()

    def has(self, stmts, models):
        """ Returns true if the statements or partial statements
        are present in the knowledge models.
        """
        raise NotImplementedError()


    def query(self, vars, patterns, models):
        raise NotImplementedError()

    def classesof(self, concept, direct, models):
        """ Returns the RDF classes of the concept.
        """
        raise NotImplementedError()

