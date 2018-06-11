# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Basic OS configuraion
  config.vm.box = "centos/7"
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.hostname = "acilab"

  config.vm.define :acilab do |acilab| # <1>
  end

  config.vm.network "forwarded_port", guest: 80, host: 8080 # <2>

  config.ssh.insert_key = true

  config.vm.provider :virtualbox do |v|
    v.name = "acilab"
    v.memory = 512 # <3>
    v.cpus = 1 # <3>
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    yum makecache
    yum install -y git # <4>
    git clone https://github.com/jacek-kosinski/aciautomationlab.git
  SHELL

  config.vm.provision "shell", # <5>
    path: "https://get.docker.com/"
  config.vm.provision "shell",
    inline: "systemctl enable docker"
  config.vm.provision "shell",
    inline: "systemctl start docker"

  config.vm.provision "docker",
    images: ["ubuntu", "centos", "jacekkosinski/acitoolkit"] # <6>

  config.vm.provision "docker" do |d|
    d.run "jacekkosinski/acilabguide", # <7>
      args: "-p 80:80"
  end
end
