import React, {Component} from 'react';

class SearchBar extends Component {
  constructor() {
    super();
    this.state = {
      term: ''
    }
  }

  onInputChange(term) {
    this.setState({term: term});
    this.props.onSearchTermChange(term);
  }

  render(){
    return (
      <div className="search-bar">
        Search: <input onChange={(event)=>this.onInputChange(event.target.value)}/>
      </div>
    );
  }
}

export default SearchBar;
