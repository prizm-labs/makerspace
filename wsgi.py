import sys

from app import app

if __name__ == "__main__":
    port = 7777
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port, debug=True)
    #app.run(host='0.0.0.0', debug=True)