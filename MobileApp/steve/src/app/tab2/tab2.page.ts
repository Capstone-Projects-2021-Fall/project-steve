import { Component } from '@angular/core';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {

  speed = 0
  turnVal = 90

  constructor() {}

  speedUp() {

  }

  slowDown() {

  }

  stop() {
    console.log('stop')
    this.speed = 0;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  routeCompleted() {

  }


  postToRemoteServer(speed, turnVal) {
    $.ajax({
      type: "POST",
      url: "http://10.226.108.80:9999/controlCar",
      data: {
        "speed": speed,
        "turnVal": turnVal
      },
      success: function(data) {
        console.log('successfully posted')
      }
    });
  }

}
