import React,{useState,useEffect} from 'react';
import axios from 'axios';
import AddTask from './AddTask';
import EditButton from './EditButton';

const Completed = () => {

  const [completedList,setCompletedList] = useState([]);  
  const [status,setStatus] = useState("completed");

  const getCompleted = async () => {
    try {
      console.log("Called");
      const response = await axios.get("http://localhost:8000/api/tasks/");
      response.data.filter( (item) => item.status === status );
      setCompletedList(response.data);
    } catch(err) {
      console.log(err.message);
    }    
  };

  const deleteTodo = async (id) => {
    await  axios.delete(`http://localhost:8000/api/tasks/${id}/`);
    getCompleted();
  };

  // onMount
  useEffect(()=>{
    getCompleted();
  },[]);

  
  
	return (
  <div className="container">    
		<h2 className='text-black text-uppercase text-center my-4'>Completed</h2>    
    <AddTask refreshList={getCompleted}/>
          {
            completedList.map((todo) => {
              return <div className="card mt-3" style={{width:'442 px'}} id={todo.todo_id}>
                <div className="card-body">
                  <h5 className="card-title">{todo.title}</h5>
                  <p className="card-text">{todo.description}</p>
                  <div className="radio"> 
                    <label><input type="checkbox" name="optradio" onClick={() => setStatus("completed")}/>Completed</label>
                  </div>
                  <div><EditButton refreshList={getCompleted}/></div>
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

export default Completed;