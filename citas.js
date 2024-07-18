const mongoose = require('mongoose')
  const url = 'mongodb://localhost:27017/citas_medicas'
  mongoose.connect(url)
  .then(()=>{
    console.log('jala')
  })
  .catch((err)=>{
    console.log('no jala')
  })

const cita =new mongoose.Schema({
    name:{
        type:String         
    },
    fecha:{
        type:String
    },
    hora:{
        type:String
    }
  })
  const cita1 =new mongoose.model('usuario', cita)
  cita1.create({
    name:"Diego",
    fecha:"16/08/2024",
    hora:"10:15"
  })