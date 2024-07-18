const mongoose = require('mongoose')
  const url = 'mongodb://localhost:27017/citas_medicas'
  mongoose.connect(url)
  .then(()=>{
    console.log('jala')
  })
  .catch((err)=>{
    console.log('no jala')
  })

  const usuario =new mongoose.Schema({
    name:{
        type:String         
    },
    curp:{
        type:String
    },
    correo:{
        type:String
    }
  })
  const usuario1 =new mongoose.model('usuario', usuario)
  usuario1.create({
    name:"Diego",
    curp:"DGNDDNGJ",
    correo:"pepe"
  })

