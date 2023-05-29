from quart import Quart, send_file, request
from get_screenshots import get_screenshot

import string, random, sys

app = Quart(__name__)

@app.route('/generate/<path:url>')
async def index(url):
    attempt_ss = get_screenshot(url)
    if attempt_ss[0] == True:
        return await send_file('temp_screenshot.png', mimetype='image/png')
    else:
        debug_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
        sys.stdout.write(f"{debug_code} - {attempt_ss[1]}\n")
        return f"Something went wrong, and your debug code is {debug_code}"

if __name__ == '__main__':
    app.run(port=1711)
