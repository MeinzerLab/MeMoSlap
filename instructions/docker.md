# Setup

- Just follow the [documentation](https://docs.docker.com/engine/install/ubuntu/#set-up-the-repository) to setup docker.
- Create the ability to run docker without sudo rights is documented [here](https://docs.docker.com/engine/install/linux-postinstall/)
  - Step 2 has to be adjusted so that $USER is the username of the person getting the permission, e.g., to give the user named `neuro-.forschung` the right to run docker without sudo:

    ```bash
    sudo usermod -aG docker neuro-forschung
    ```
