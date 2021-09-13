# S.T.E.V.E.

## System Overview

Self-driving Totally Electronic Vehicular Escort, or STEVE for short, is a fully autonomous RC car that can navigate to a predetermined location in any large indoor complex. Whether the indoor complex is a large office, a school, or an airport, STEVE will navigate the user, avoiding any obstacles along the way, and lead them to their destination courteously. The user will have an option to either use a mobile application or an Amazon Alexa enabled device to communicate with STEVE. STEVE will then use an onboard speaker to communicate any necessary messages with the user. An alternative option to make STEVE more accessible for users who have disabilities would be to grab a tether that is attached to the car.

The car will use an onboard Raspberry Pi and receiver card to communicate with a remote Python server, sending information about STEVE’s current state. The Python server will use certain libraries such as TensorFlow and OpenCV that will then process the information and decide STEVE’s next movements. The server will also send the general directions to the location to STEVE, if it knows how to get there. In addition to the Raspberry Pi and the receiver card, onboard the car there will also be a camera (to take visual input) and a speaker (to convey messages to users). In terms of storing routes, a Firebase Realtime Database will be used for long term storage. Finally, the mobile application will be built using Ionic (a web framework for building mobile apps), as well as an Amazon Alexa skill for users to be able to interact with STEVE and tell him where to go.

As time goes by and civilization advances more and more, infrastructure is advancing at an incredible rate. New buildings of all shapes and sizes are being built all the time. This is amazing for countless reasons, including getting to look at pretty skylines, but it means navigating throughout these building is getting more and more difficult. 

Usually, whenever someone goes to a new building for the first time, they do so with some sort of purpose in mind. Whether they are arriving at an office building for a business meeting or an airport in a foreign country to fly back home, they have a destination within the building in mind. If they are lucky, this destination will have a standard room number that tells them which floor it is on, but even then, it is hard to know where on the floor it is. Then you must also account for the many times where there are not standard room numbers, and someone needs to find “Mr. Doe’s Office” or “Room Garfield”. All in all, it is generally very difficult to know exactly where you are supposed to go whenever you enter a new building. 

This is where STEVE comes in. It eliminates that anxiety someone gets when they walk in a building for the first time and have no idea where they are going. It eliminates that fear of being late to a business meeting or missing a flight due to getting lost. STEVE guides people so they can worry about other things. 


## Contributors

Blake Patterson <br>
Garrett Bowser <br>
Hunter Nuss <br>
Marcel Millan <br>
Tarekegne Aboye <br>
