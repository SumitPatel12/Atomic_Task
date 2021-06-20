import React,{ useState} from 'react';
import axios from 'axios';

const AddTask = ({ refreshList }) => {

    const [title,setTitle] = useState("");
    const [description,setDescription] =useState("");
    const [status,setStatus] = useState("todo");

    const handleSubmit = async() => {
        const item = {
            "title" : title,
            "description": description,
            "status": status
        };
        try {
            await axios.post(`http://localhost:8000/api/tasks/`, item);
            refreshList();
        } catch (err) {
            console.log(err.message);
            
        }
    }

    return (<div>
        <button 
            type="button" 
            className="btn btn-success" style={{alignItems : 'center'}} 
            data-toggle="modal" 
            data-target="#myModal">
                +
            </button>
        <div className="container">                      
        
            <div className="modal fade" id="myModal" role="dialog">
                <div className="modal-dialog">
                
                
                <div className="modal-content">
                    <div className="modal-header">
                        <h4 className="modal-title">Add Task</h4>
                        <button type="button" className="close" data-dismiss="modal">&times;</button>                        
                    </div>
                    <div className="modal-body">
                        <div className="form-group">
                            <label htmlFor="title">Title</label>
                            <input 
                                className ="form-group"
                                type="text" 
                                name="title" value={title} 
                                onChange={ (e) => setTitle(e.target.value)} 
                                placeholder="Task Title" />
                        </div>
                        <div className="form-group">
                            <label htmlFor="description">Description</label>
                            <input 
                                className ="form-group"
                                type="text" 
                                name="description" value={description} 
                                onChange={ (e) => setDescription(e.target.value)} 
                                placeholder="Task Description" />
                        </div>
                        <div className="form-group">
                            <lable htmlFor="status">Status</lable>
                            <select className="from-control" id="status" name="status" onChange={(e) => setStatus(e.target.value)}>
                                <option value="todo"></option>
                                <optoin value="Inprogress"></optoin>
                                <option value="completed"></option>
                            </select>
                        </div>
                    </div>
                    <div className="modal-footer">
                    <button type="button" className="btn btn-success" onClick={handleSubmit}>Add</button>
                        <button type="button" className="btn btn-danger" data-dismiss="modal">Close</button>
                    </div>
                </div>
                
                </div>
            </div>
        
        </div>
    </div>)
}

export default AddTask;