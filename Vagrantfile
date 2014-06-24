# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "gongaloo_saucy"
  config.vm.box_url = "https://www.dropbox.com/s/6p8sf4j1fyqwjtx/gongaloo_saucy.box?dl=1"

  config.vm.network :private_network, ip: "192.168.33.105"
  config.vm.synced_folder "./", "/var/local/sites/gongaloo/local_src",
      owner:"gongaloo",
      group:"vagrant"

      

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deployment/site.yml"
    ansible.inventory_path = "hosts"
    ansible.verbose = "v"
  end
end
