const prompt = require("prompt-sync")({
  sigint: true,
  eot: true,
});

const { doDishes, takeOutTrash, sweepFloors } = require("./home/chores.js");
const { washVegetables, chopMeat } = require("./home/cook.js");
const { playGames, petDog, readBook, takeNap } = require("./home/leisure.js");

const { code, attendMeeting, updateSchedule } = require("./office/work.js");
const { chat, getWater, useSocialMedia } = require("./office/idle.js");
const { exit } = require("process");

const morningMenu = () => {
  console.log("Starting the day off...");
  while (true) {
    console.log(
      "\nWhat do you want to do? \n1: Take out trash\n2: Sweep the floor\n3: Go to work\n4: Quit"
    );
    let choice = prompt("> ");
    if (choice === "1") {
      takeOutTrash();
    } else if (choice === "2") {
      sweepFloors();
    } else if (choice === "3") {
      console.log("Going to work...");
      workMenu();
      break;
    } else if (choice === "4") {
      console.log("Bye!");
      exit(-1);
    } else {
      console.log("Please enter a valid input");
    }
  }
};

const workMenu = () => {
  while (true) {
    console.log(
      "\nWhat do you want to do? \n1: Code\n2: Attend meeting\n3: Update schedule\n4: Slack off\n5: Go Home\n6: Quit"
    );
    let choice = prompt("> ");
    if (choice === "1") {
      code();
    } else if (choice === "2") {
      attendMeeting();
    } else if (choice === "3") {
      updateSchedule();
    } else if (choice === "4") {
      slackOffMenu();
      break;
    } else if (choice === "5") {
      console.log("Going home...\n");
      eveningMenu();
      break;
    } else if (choice === "6") {
      console.log("Bye!");
      exit(-1);
    } else {
      console.log("Please enter a valid input");
    }
  }
};

const slackOffMenu = () => {
  while (true) {
    console.log(
      "\nWhat do you want to do? \n1: Chat\n2: Get water\n3: Use social media\n4: Back to work\n5: Quit"
    );
    let choice = prompt("> ");
    if (choice === "1") {
      chat();
    } else if (choice === "2") {
      getWater();
    } else if (choice === "3") {
      useSocialMedia();
    } else if (choice === "4") {
      workMenu();
      break;
    } else if (choice === "5") {
      console.log("Bye!");
      exit(-1);
    } else {
      console.log("Please enter a valid input");
    }
  }
};

const eveningMenu = () => {
  while (true) {
    console.log(
      "\nWhat do you want to do? \n1: Chores\n2: Leisure\n3: Sleep\n4: Quit"
    );
    let choice = prompt("> ");
    if (choice === "1") {
      choresMenu();
    } else if (choice === "2") {
      leisureMenu();
    } else if (choice === "3") {
      console.log("Going to sleep...\n\n\n\n");
      console.log("Waking up the next morning...");
      morningMenu();
    } else if (choice === "4") {
      console.log("Bye!");
      exit(-1);
    } else {
      console.log("Please enter a valid input");
    }
  }
};

const choresMenu = () => {
  while (true) {
    console.log(
      "\nWhat do you want to do? \n1: Do dishes\n2: Wash vegetables\n3: Chop meat\n4: Return to evening menu\n5: Quit"
    );
    let choice = prompt("> ");
    if (choice === "1") {
      doDishes();
    } else if (choice === "2") {
      washVegetables();
    } else if (choice === "3") {
      chopMeat();
    } else if (choice === "4") {
      eveningMenu();
    } else if (choice === "5") {
      console.log("Bye!");
      exit(-1);
    } else {
      console.log("Please enter a valid input");
    }
  }
};

const leisureMenu = () => {
  while (true) {
    console.log(
      "\nWhat do you want to do? \n1: Play games\n2: Pet dog\n3: Read book\n4: Take nap\n5: Return to evening menu\n6: Quit"
    );
    let choice = prompt("> ");
    if (choice === "1") {
      playGames();
    } else if (choice === "2") {
      petDog();
    } else if (choice === "3") {
      readBook();
    } else if (choice === "4") {
      takeNap();
    } else if (choice === "5") {
      eveningMenu();
    } else if (choice === "6") {
      console.log("Bye!");
      exit(-1);
    } else {
      console.log("Please enter a valid input");
    }
  }
};

morningMenu();