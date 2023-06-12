from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

html = '''
<html>
<head>
    <title>Image Display</title>
    <style>
        .image-container {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="image-container">
        <img id="image" src="{{ image_url }}" alt="Image" onclick="get_coordinates(event)">
    </div>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        function get_coordinates(event) {
            var rect = event.target.getBoundingClientRect();
            var x = event.clientX - rect.left;
            var y = event.clientY - rect.top;
            var coordinates = 'x: ' + x + ', y: ' + y;
            console.log(coordinates);

            $.ajax({
                url: '/get_coordinates',
                type: 'POST',
                data: {x: x, y: y},
                success: function(response) {
                    console.log(response);
                }
            });
        }
    </script>
</body>
</html>
'''


@app.route('/')
def index():
    image_url = "/static/images/image.jpg"  # 이미지 파일의 경로
    return render_template_string(html, image_url=image_url)


@app.route('/get_coordinates', methods=['POST'])
def get_coordinates():
    x = request.form['x']
    y = request.form['y']
    print('Clicked at coordinates: x={}, y={}'.format(x, y))
    return jsonify({'message': 'Coordinates received'})


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=False)

