const chat = () => {
    const coworkers = ["Jack", "Lenny", "Michelle", "Andrea"];
    let chatee = coworkers[Math.floor(Math.random()*4)];
    console.log("Chatting with " + chatee + "...");
    console.log("Done");
}

const getWater = () => {
    console.log("Getting water...");
    console.log("That was refreshing.");
}

const useSocialMedia = () => {
    const socialMedia = ["FaceBook", "Twitter", "YouTube", "Reddit"];
    let choice = socialMedia[Math.floor(Math.random()*4)];
    console.log("Using " + choice + "...");
    console.log("Done");
}

module.exports = {
    chat,
    getWater,
    useSocialMedia
}