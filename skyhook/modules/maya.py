import json
try:
    import pymel.core as pm
    print("was able to import pymel")
    import maya.cmds as cmds
except:
    pass

def make_cube():
    """
    Example function that will make a cube named Nisse

    :return:
    """
    pm.polyCube(name="Nisse")

def make_sphere(name="Nisse"):
    """
    Example function that will make a sphere name Nisse

    :return:
    """
    pm.polySphere(name=name)
    return "I made a sphere"

def raw_maya(command, args=[], kwargs={}):
    """
    Handle a "raw" maya.cmds or pymel command. Expects args to be a list and kwargs to be a dictionary.

    Eg::
    import skyhook.client
    maya_client = skyhook.client.MayaClient()
    maya_client.execute("raw_maya", {"command": "pm.polySphere", "kwargs": {"radius": 20}})


    :param command: *string* of complete command. eg: pm.ls or cmds.polyCube
    :param args: *list* of unnamed arguments
    :param kwargs: *dict* with keywords that are needed for your command
    :return: *string* of whatever the command returned in Maya
    """
    kwargs = dict((str(k), v) for k, v in kwargs.items())
    func = eval(command)
    print(kwargs)


    result = func(*args, **kwargs)
    return str(result)

def execute_python(python_script):
    """
    Executes a complete Python script

    :param python_script: *string* Python code
    :return: None
    """
    exec(python_script)

def warning(message):
    pm.warning(message)