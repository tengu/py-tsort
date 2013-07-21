all:

clean:
	rm -fr *.egg-info dist build *.egg *.pyc
scrub: clean
	rm -fr $(ve)

#ve_opt=--system-site-packages
ve=$(PWD)/ve
python=$(ve)/bin/python
ve: $(ve)
$(ve):
	virtualenv $(ve_opt) $@

install: $(ve)
	$(python) setup.py install
test: $(ve)
	$(python) setup.py test
develop:
	$(python) setup.py develop
push: $(ve)
	$(python) setup.py sdist register upload

###

t:
	$(python) test.py
