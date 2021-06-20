import React,{useState,useEffect} from 'react';
import axios from 'axios';
import AddTask from './AddTask';
import EditButton from './EditButton';

const InProgress = () => {

  const [inprogressList,setInProgressList] = useState([]);  
  const [status,setStatus] = useState("Inprogress");

  const getInProgress = async () => {
    try {
      console.log("Called");
      const response = await axios.get("http://localhost:8000/api/tasks/");
      response.data.filter( (item) => item.status === status );
      setInProgressList(response.data);
    } catch(err) {
      console.log(err.message);
    }    
  };

  const deleteTodo = async (id) => {
    await  axios.delete(`http://localhost:8000/api/tasks/${id}/`);
    getInProgress();
  };

  // onMount
  useEffect(()=>{
    getInProgress();
  },[]);

  
  
	return (
  <div className="container">    
		<h2 className='text-black text-uppercase text-center my-4'>In Progress</h2>    
    <AddTask refreshList={getInProgress}/>
          {
            inprogressList.map((todo) => {
              return <div className="card mt-3" style={{width:'442 px'}} id={todo.todo_id}>
                <div className="card-body">
                  <h5 className="card-title">{todo.title}</h5>
                  <p className="card-text">{todo.description}</p>
                  <div className="radio"> 
                    <label><input type="checkbox" name="optradio" onClick={() => setStatus("completed")}/>Completed</label>
                  </div>
                  <div><EditButton refreshList={getInProgress}/></div>
                  <div>
                    <button className="btn btn-danger" onClick={() => deleteTodo(todo.todo_id)}>
                      Delete
                    </button>
                  </div>
                </div>                
              </div>
            })
          }                  
	</div>);
	
}

export default InProgress;