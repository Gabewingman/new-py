let grades = {
    Math: 90,
    English: 85,
    Filipino: 89,
    Mapeh: 92,
    Science: 87,
    AP:97
};

let average = 0;

for(let subject in grades){
    console.log(`${subject} : ${grades[subject]}`);
    average += grades[subject]
}

average /= Object.keys(grades).length;
console.log('');
console.log(`Average : ${average}`);

