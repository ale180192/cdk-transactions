

# Testing endpoints

We create the virtual env, we install dependencies and run the local server at port 80
```
# on Mac/linux
cd transactions_backend
python3 venv .env
pip install -r requirements.tx
source .venv/bin/activate
cd src
PYTHONPATH=. python djangoapp/manage.py runserver 0.0.0.0:80
```

### GET api/transactions/v1/companies
```
curl --location --request GET 'http://localhost:80/api/transactions/v1/companies/aa8c217b320849e38ac0b02c57209ca8'
```

### GET api/transactions/v1/companies
```
curl --location --request GET 'http://localhost:80/api/transactions/v1/summary'
```


# Django Project


### Django project run local - best way!!

```bash
cd transactions_backend/src
PYTHONPATH=. python djangoapp/manage.py runserver 0.0.0.0:80
```

### Django project run with docker compose
```bash
cd transactions_backend
docker-compose up
```

### Utils Django commands
PYTHONPATH=. python djangoapp/manage.py makemigrations --name load_csv_to_database transact --empty
PYTHONPATH=. python djangoapp/manage.py migrate transact 0001_initial
PYTHONPATH=. python djangoapp/manage.py flush --noinput

# AWS CDK - Infraestructure

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

### Deploy
make sure to set the correct env with before does the deploy
```bash
export ENV_FOR_DYNACONF=default
cdk deploy
```
