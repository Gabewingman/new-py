let family = {
    firstName:["Gabby","Ron","Teresita"], //<-Array
    lastName:"Bersamina",
    //Nested list of JSON(JSON inside JSON)
    pets:{
        1:{
            Name:"Ash",
            Type:"Cat",
            Breed:"Pinoy Cat"
        },
        2:{
            Name:"Bruce",
            Type:"Cat",
            Breed:"Pinoy Cat"
        }
    }
};

//JSON stringify. key|value to string
console.log(family);
let strfamily = JSON.stringify(family);
console.log(strfamily);

//JSON parsing. String to key|value
let strPet = `{"Name":"Ash","Type":"Cat","Breed":"Pinoy Cat"}`;
let Cat = JSON.parse(strPet);
console.log(Cat);

//JSON write. Update existing key|value
family["firstName"] = ["Harold","Gale","Nelson"];
family["middleName"] = ["Pulido"];

//JSON write. Create/Add new key|value
console.log(family.middleName);

//console of a JSON read file either both
console.log(family.firstName);
console.log(family["firstName"]);

//Using JSON read for Array
console.log(family["firstName"][0]);

//JSON read file when accesing JSON file inside JSON file, either both
console.log(family["pets"][1]["Breed"]);
console.log(family.pets[1].Breed);

//JSON array
let friends = [
    {
        firstName:"Harold",
        lastName:"Radona",
        status:"Married"
    },
    {
        firstName:"Gale",
        lastName:"Francisco",
        status:"Single"
    },
    {
        firstName:"Milboy",
        lastName:"Diaz",
        status:"Single"
    }
];

for(i = 0;i < friends.length;i++){
    console.log(friends);
}
