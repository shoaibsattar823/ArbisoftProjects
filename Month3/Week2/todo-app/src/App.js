import React, { Component } from 'react';
import './App.css';

class ToDoList extends Component {
  constructor(){
    super();
    this.state = {
      item: null,
    };
  }

  render() {
    return (
      <div>
        <div>
          <label htmlFor="todo">Enter Your Task </label>
          <input className="inputClass" id="todo"/>
          <button className="submitClass" id="sbmt" onClick={()=>this.setState({item:document.getElementById("todo").value})}>Enter</button>
        </div>
        <div>
          <Insert item={this.state.item} />
        </div>
      </div>
    );
  }

}

class Insert extends Component{
  constructor(){
    super();
    this.state = {
      items: []
    };
  }

  insertItem(item){
    let arr = this.state.items;
    arr.push({
      text: this.props.item,
      key: Date.now()
    });
  }

  render(){
    if (this.props.item !== null && this.props.item !== ""){
      this.insertItem(this.props.item);
    }
    let entries = this.state.items;
    function createTasks(item){
      return <li key={item.key}>{item.text}</li>
    }
    let listItems = entries.map(createTasks);
    return (
      <ul>{listItems}</ul>
    );
  }
}

class App extends Component{
  render(){
    return <ToDoList />;
  }
}
export default App;
