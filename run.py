"""
Search App
Version: 0.1.0
"""

import os
import argparse
from app.app import app


"""
Run webserver
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Start webserver.')
    parser.add_argument('-p', '--port',
                        type=int,
                        default=8080,
                        help='Port number for webserver.')

    args = parser.parse_args()
    port = os.environ.get("PORT", args.port)
    app.run(host='0.0.0.0', port=port)
