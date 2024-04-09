let person = {
    firstName:"Peter Gabriel",
    middleName:"Pulido",
    lastName:"Bersamina",
    age:23
}

//Using for-in loop inside JSON file
for(let kv in person){
    console.log(person[kv]);
}

//Object Keys. Use a object keys tags to view your output into an array format
let keys = Object.keys(person);
console.log(keys);