build: adcleaner.py adcleaner.spec
	pyinstaller adcleaner.spec

clean:
	rm -r build/ dist/