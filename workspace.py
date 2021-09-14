#  import docker
#  from deepo.generator.generate import generate, _import
#  from deepo.generator.modules import pytorch

from src.__main__ import *
generate("https://github.com/norvig/pytudes")


#  import string
#  import os
#  client = docker.DockerClient(base_url='unix://var/run/docker.sock')

#  base_image = "pytorch"
#  workspace_name = "vscode"
#  workspace_dockerfile = f"Dockerfile.{workspace_name}"

#  modules = base_image.split(" ")
#  tagname = ""
#  for module in modules:
    #  tagname += module

#  dockerfile_name = f"Dockerfile.{workspace_name}.{tagname}"
#  dockerfile_path = f"./images/{dockerfile_name}"
#  args = {
    #  'workspace': workspace_name,
    #  'path': dockerfile_path,
    #  'modules': modules,
    #  'cuda_ver': None,
    #  'cudnn_ver': None,
    #  'ubuntu_ver': '18.04'
#  }
#  generate(args)


#  counter = 0
#  data = ""
#  with open(dockerfile_path, "rb+") as f:
    #  responses = [line for line in client.api.build(fileobj=f, rm=True, tag=tagname)]
    #  #  print(responses)

#  final_workspace_image_path = f"./final-images/{workspace_dockerfile}"
#  final_workspace_image = open(final_workspace_image_path, "rb+")
#  final_workspace_image_data = final_workspace_image.read()

#  final_image_path = f"./tar/{workspace_name}/{dockerfile_name}"
#  with open(final_image_path, "wb+") as final_image:
    #  final_image_data = f"FROM {tagname}\n".encode("UTF-8")
    #  final_image_data += final_workspace_image_data
    #  final_image.write(final_image_data)


#  #  #  with open(dockerfile_path, "rb+") as f:
    #  #  #  dockerfile_contents = f.read()

#  tagname = f"manosriram/{workspace_name}-{tagname}"
#  build_args = {
    #  'PIPELINE': 'build'
#  }

#  path = os.path.dirname(os.getcwd())
#  path += f"/workspaces/tar/{workspace_name}"
#  with open(final_image_path, "rb+") as f:
    #  responses = [line for line in client.images.build(path=path, dockerfile=dockerfile_name, rm=True, tag=tagname)]
    #  print(responses)

#  #  client.login(username='manosriram', password='#<3web_dev')
#  #  for line in client.api.push('manosriram/vscode-pytorch:latest', stream=True, decode=True):
    #  #  print(line)

