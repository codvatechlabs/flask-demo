from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def run_program():
    try:
        arg1 = request.json['arg1']
        arg2 = request.json['arg2']
        arg3 = request.json['arg3']

        # Construct the command to run your Python program
        command = f"python3 demo.py {arg1} {arg2} {arg3}"

        # Execute the command using subprocess
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            output = result.stdout
            return jsonify({'output': output})
        else:
            error = result.stderr
            return jsonify({'error': error}), 500
    except KeyError:
        return jsonify({'error': 'Invalid JSON data. Make sure you provide "arg1," "arg2," and "arg3".'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
