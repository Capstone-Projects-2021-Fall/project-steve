import { Component } from '@angular/core';
import * as $ from "jquery";
import { initializeApp } from 'firebase/app';
import { getDatabase, ref, onValue, set} from "firebase/database";

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {

  speed = 0
  turnVal = 90
  
  write_to_firebase() {
	  const db = getDatabase();
		var suc = set(ref(db, 'car_data'), {
			speed : this.speed,
			turnVal : this.turnVal
		});
		if(suc) {
			console.log("Successfully wrote to firebase");
		} else {
			console.log("Unable to write to firebase");
		}
  }

  constructor() {
	  const firebaseConfig = {
      apiKey: "AIzaSyCiBPkwDTFuiOrRtKc3ZKUAh_xwvSb8WSI",
      authDomain: "steve-2efa6.firebaseapp.com",
      databaseURL: "https://steve-2efa6-default-rtdb.firebaseio.com",
      projectId: "steve-2efa6",
      storageBucket: "steve-2efa6.appspot.com",
      messagingSenderId: "650370236834",
      appId: "1:650370236834:web:0bca880b2938e86c04f2fb",
      measurementId: "G-LJ8TNR05TL"
    };
  
    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
	
	 	
  }

 

  forward() {
    console.log('forward')
    this.speed = .12;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  left() {
    console.log('left')
    this.turnVal = 180;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  center() {
    console.log('center')
    this.turnVal = 90;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  right() {
    console.log('right')
    this.turnVal = 0;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  stop() {
    console.log('stop')
    this.speed = 0;
    this.postToRemoteServer(this.speed, this.turnVal);
  }

  postToRemoteServer(speed, turnVal) {
	this.write_to_firebase();
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
