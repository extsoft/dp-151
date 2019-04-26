
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu1804"
  config.vm.define "dp-151"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provision :docker
  config.vm.provision :docker_compose
  config.vm.provider "virtualbox" do |v|
    v.name = "dp-151_app"
  end
end