# Run API file

import coinApp.main
from coinApp import app,api



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
