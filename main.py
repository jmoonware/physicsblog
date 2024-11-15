# use this file for starting a local server for test

import project

# entry point
def main():
	project.app.run_server(debug=True)

if __name__=="__main__":
	main()
