import React,{useState} from 'react'
import axios from 'axios';

const  EditButton = ({ refreshList,todo_id,user_id }) => {
    
    const [title,setTitle] = useState("");
    const [description,setDescription] =useState("");
    const completed= false;

    const handleSubmit = async() => {
        const item = {
            todo_id: todo_id,
            user_id: user_id,
            title : title,
            description: description,
            completed: completed
        };
        try {
            await axios.put(`http://localhost:8000/task/update-task/${todo_id}`, item);
            refreshList();
        } catch (err) {
            console.log(err.message);
            
        }
    }

    return (<div>
        <button 
            type="button" 
            className="btn btn-success" 
            data-toggle="modal" 
            data-target="#myModal">
                Edit
            </button>
        <div className="container">                      
        
            <div className="modal fade" id="myModal" role="dialog">
                <div className="modal-dialog">
                
                
                <div className="modal-content">
                    <div className="modal-header">
                        <button type="button" className="close" data-dismiss="modal">&times;</button>
                        <h4 className="modal-title">Edit Task</h4>
                    </div>
                    <div className="modal-body">
                        <div className="form-group">
                            <label htmlFor="title">Title</label>
                            <input 
                                type="text" 
                                name="title" value={title} 
                                onChange={ (e) => setTitle(e.target.value)} 
                                placeholder="Task Title" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="description">Title</label>
                            <input 
                                type="text" 
                                name="description" value={description} 
                                onChange={ (e) => setDescription(e.target.value)} 
                                placeholder="Task Description" />                    
                        </div>
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-success" onClick={handleSubmit}>Edit</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
                    </div>
                </div>
                
                </div>
            </div>
        
        </div>
    </div>);
};

export default EditButton;