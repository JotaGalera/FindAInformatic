
Vagrant.configure("2") do |config|

  config.vm.define "FindAInformatic" do |findainformatic|

  findainformatic.vm.box = "google/gce"
  findainformatic.vm.synced_folder "~/Escritorio/FindAInformatic/", "/home/vagrant/"


        findainformatic.vm.provider :google do |google, override|
          google.name = "findainformatic1"
          google.google_project_id = "findainformatic"
          google.google_client_email = "javier@findainformatic.iam.gserviceaccount.com"
          google.google_json_key_location = "/home/jota/Escritorio/FindAInformatic/data.json"

          google.image_family = 'ubuntu-1604-lts'

          override.ssh.username = "jota"
          override.ssh.private_key_path = "~/.ssh/google_compute_engine"

        end

        findainformatic.vm.provision "ansible" do |ansible|
          ansible.become = true
          ansible.verbose = "vvvv"
          ansible.playbook = "ansible/playbook.yml"
        end

  end
end
