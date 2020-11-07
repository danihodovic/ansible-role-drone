# ansible-role-drone [![Build Status](https://ci.depode.com/api/badges/danihodovic/ansible-role-drone/status.svg)](https://ci.depode.com/danihodovic/ansible-role-drone)

Deploys [Drone CI](https://drone.io/)

### Testing

Create a virtual env and install the dependencies
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a Gitlab account and an oauth application. Follow the instructions on
the [Drone docs](https://docs.drone.io/server/provider/gitlab/).

Once the OAuth application is created expose the below variables in your
environment.

```sh
export GITLAB_CLIENT_ID=id
export GITLAB_CLIENT_SECRET=secret
```

Run molecule
```
mocule test
```
