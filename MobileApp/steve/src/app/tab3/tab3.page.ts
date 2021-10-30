import { Component } from '@angular/core';
import { initializeApp } from 'firebase/app';
import { getDatabase, ref, onValue} from "firebase/database";

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss']
})
export class Tab3Page {

  routes: JSON[];

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

    const db = getDatabase();
    const routeRef = ref(db, 'route');
    onValue(routeRef, (snapshot) => {
      const data = snapshot.val();
      console.log(data)
      var result = [];

      for(var i in data){
        console.log(data[i])
        result.push(data[i]);
      }

      this.routes = result;

    });

  }

}
