import { Component } from '@angular/core';
import * as $ from "jquery";

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {

  speed = 0
  turnVal = 90

  constructor() {}

  forward() {
    console.log('forward')
    this.speed = .12;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  left() {
    console.log('left')
    this.turnVal = 0;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  center() {
    console.log('center')
    this.turnVal = 90;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  right() {
    console.log('right')
    this.turnVal = 180;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  stop() {
    console.log('stop')
    this.speed = 0;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  postToRemoteServer(speed, turnVal) {
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:9999/controlCar",
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
