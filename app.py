import dash
from dash import html, dcc
import dash_pannellum

app = dash.Dash(__name__)
server = app.server  # 这一行很重要，Vercel需要它

tour_config = {
    "default": {
        "firstScene": "street A",
        "sceneFadeDuration": 1000,
    },
    "scenes": {
        "street A": {
            "title": "Street A",
            "hfov": 100,
            "pitch": -1,
            "yaw": 0,
            "type": "equirectangular",
            "panorama": "/assets/Tan Panorama.png",
            "autoLoad": True,
            "hotSpots": [
                {
                    "pitch": -2.1,
                    "yaw": 2,
                    "type": "scene",
                    "text": "Between street A & B",
                    "sceneId": "street A-B"
                }
            ]
        },
        "street A-B": {
            "title": "Between street A & B",
            "hfov": 100,
            "yaw": 0,
            "type": "equirectangular",
            "panorama": "/assets/street-AB.jpg",
            "autoLoad": True,
            "hotSpots": [
                {
                    "pitch": 0,
                    "yaw": -1,
                    "type": "scene",
                    "text": "Street B",
                    "sceneId": "street B",
                    "targetPitch": 0,
                    "targetYaw": 0,
                },
                {
                    "pitch": 180,
                    "yaw": -1,
                    "type": "scene",
                    "text": "Street A",
                    "sceneId": "street A",
                    "targetYaw": 180,
                    "targetPitch": 0,
                }
            ]
        },
        "street B": {
            "title": "Street B",
            "hfov": 100,
            "yaw": 0,
            "type": "equirectangular",
            "panorama": "/assets/street-B.jpg",
            "autoLoad": True,
            "hotSpots": [
                {
                    "pitch": 0,
                    "yaw": 180,
                    "type": "scene",
                    "text": "Between street A & B",
                    "sceneId": "street A-B",
                    "targetYaw": 180,
                    "targetPitch": 0
                }
            ]
        }
    }
}

app.layout = html.Div([
    html.H1("Mental Map Experiment_1"),
    html.Script('''
        (function(h,o,t,j,a,r){
            h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
            h._hjSettings={hjid:6410021,hjsv:6};
            a=o.getElementsByTagName('head')[0];
            r=o.createElement('script');r.async=1;
            r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
            a.appendChild(r);
        })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
    ''', type='text/javascript'),
    dash_pannellum.DashPannellum(
        id='tour-component',
        tour=tour_config,
        customControls=True,
        showCenterDot=True,
        width='100%',
        height='750px',
        autoLoad=True,
        compass=True,
        northOffset=90
    ),
])

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True, port='8051')