const {RichEmbed} = require("discord.js");
var fs = require('fs');
var request = require("request");
const SteamAPI = require('steamapi');
const api = new SteamAPI("F5B1143BAD6BAD00EBBF0805DA004318");

api.getUserSummary(steamID).then(summary => {
    console.log('QQQ');
    var nickname = summary.nickname;
    if (nickname.includes('SAO')) {
        client.database = {[message.author.id]: steamID}
        fs.writeFile("./database.json", JSON.stringify(client.database, null, 4), err => {
            if (err) throw err;
            message.channel.send("Steam ID Verified!");
            console.log(message.author.id + " verified with the steam id of " + steamID);
        });
    } else {
        message.channel.send("Please add '**SAO**' to your steam name and run the command again.");
        message.channel.send("This can be done here https://steamcommunity.com/profiles/" + steamID + "/edit");
    }
});