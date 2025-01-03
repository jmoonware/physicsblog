# use this file for starting a local server for test

import project_jtp

# entry point
def main():
	project_jtp.app.run_server(debug=True)

if __name__=="__main__":
	main()
