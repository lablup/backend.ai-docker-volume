from bottle import request, route


def list_volumes():
    raise NotImplemented
    # return {'Volumes': [{'Name': basename(v)} for v in volumes], 'Err': ''}


@route('/Plugin.Activate', ['POST'])
def plugin_activate(req):
    return {'Implements': ['VolumeDriver']}


@route('/VolumeDriver.Create', ['POST'])
def volume_create(req):
    name = req['Name']
    opts = req['Opts']
    # return {'Err': ''}


@route('/VolumeDriver.Remove', ['POST'])
def volume_remove(req):
    name = req['Name']
    # return {'Err': ''}


@route('/VolumeDriver.Mount', ['POST'])
def volume_mount(req):
    name = req['Name']
    id = req['ID']
    path = 'to-be-determined'
    if path is None:
        return {'Err': f'{name}: no such volume'}
    return {'Mountpoint': path, 'Err': ''}


@route('/VolumeDriver.Path', ['POST'])
def volume_path(req):
    name = req['Name']
    path = 'to-be-determined'
    if path is None:
        return {'Err': f'{name}: no such volume'}
    return {'Mountpoint': path, 'Err': ''}


@route('/VolumeDriver.Unmount', ['POST'])
def volume_unmount(req):
    name = req['Name']
    id = req['ID']
    return {'Err': ''}


@route('/VolumeDriver.Get', ['POST'])
def volume_get(req):
    name = req['Name']
    path = 'to-be-determined'
    if path is None:
        return {'Err': '{}: no such volume'.format(name)}
    return {'Volume': {'Name': name, 'Mountpoint': path}, 'Err': ''}


@route('/VolumeDriver.List', ['POST'])
def volume_list(req):
    return list_volumes()


@route('/VolumeDriver.Capabilities', ['POST'])
def driver_cap(req):
    # return {"Capabilities": {"Scope": "local"}}
