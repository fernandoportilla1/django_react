import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link, Route, Switch } from 'react-router-dom';


class App extends Component {
    render() {
        // var data = this.props.data
        // console.log(this.props);
        // console.log(data);

        return (
            <div>
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route path="/company" component={Products} />
                    <Route path="/category" component={Category} />
                </Switch>

            </div>
        );
    }
}


/*Home component */
const Home = (props) => (
    <div>
        <h2>Home {console.log(props)}</h2>
    </div>
)

/*Product component */
const Products = (props) => (
    <div>
        <h2>Company</h2>
    </div>
)

/*Category component*/
const Category = () => (
    <div>
        <h2>Category</h2>
    </div>
)



export default App;
