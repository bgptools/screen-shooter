from quart import Quart, send_file, request
from get_screenshots import get_screenshot

import string, random

app = Quart(__name__)

# Enable this to activate logs for when shit goes wrong
debug_logs = True

@app.route('/generate/<path:url>')
async def index(url):
    attempt_ss = get_screenshot(url)
    if attempt_ss[0] == True:
        return await send_file('temp_screenshot.png', mimetype='image/png')
    else:
        if debug_logs == True:
            with open('logs.txt', 'a') as file:
                debug_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=24))
                file.write(f"{debug_code} - {attempt_ss[1]}")
                return f"Something went wrong, and your debug code is {debug_code}"
        else:
            return "Something went wrong. Debugging logs are not enabled, so you do not have a code."

if __name__ == '__main__':
    app.run(port=1711)
