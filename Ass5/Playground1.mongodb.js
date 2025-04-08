// Select the database to use.
use('Sigma');

// Insert a few documents into the sales collection without specifying `_id`.
db.getCollection('Humans').insertMany([
    {
      "name": "Omkar",
      "height": "5'4",
      "value": 0
    },
    {
      "name": "Aarav",
      "height": "5'6",
      "value": 1
    },
    {
      "name": "Priya",
      "height": "5'3",
      "value": 0
    },
    {
      "name": "Saanvi",
      "height": "5'5",
      "value": 2
    },
    {
      "name": "Ankit",
      "height": "5'8",
      "value": 1
    },
    {
      "name": "Riya",
      "height": "5'2",
      "value": 0
    },
    {
      "name": "Raj",
      "height": "5'9",
      "value": 3
    },
    {
      "name": "Neha",
      "height": "5'7",
      "value": 1
    },
    {
      "name": "Karan",
      "height": "5'10",
      "value": 2
    },
    {
      "name": "Meera",
      "height": "5'4",
      "value": 0
    }
]);

// Print a success message.
console.log("Data Insertion Done");
