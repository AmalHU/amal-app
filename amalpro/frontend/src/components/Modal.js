import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, defaultvalue } = e.target;

    // if (e.target.type === "checkbox") {
    //   value = e.target.checked;
    // }

    const activeItem = { ...this.state.activeItem, [name]: defaultvalue};
    this.setState({ activeItem });
  };
  
  onChange = (event) => this.setState({ value: event.target.value });

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Customer Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="customer-name">Full Name</Label>
              <Input
                type="text"
                id="customer-name"
                name="name"
                defaultvalue={this.state.value}
                onChange={this.handleChange}
                placeholder="Enter Customers Full Name"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-cnic">CNIC Number</Label>
              <Input
                type="text"
                id="customer-cnic"
                name="cnic"
                defaultvalue={this.state.activeItem.value}
                onChange={this.handleChange}
                placeholder="42201-3748392-7"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-address">Address</Label>
              <Input
                type="text"
                id="customer-address"
                name="address"
                defaultvalue={this.state.activeItem.value}
                onChange={this.handleChange}
                placeholder="A-245, Block-5, Gulshan-e-Iqbal"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-city">City</Label>
              <Input
                type="text"
                id="customer-city"
                name="city"
                defaultvalue={this.state.activeItem.value}
                onChange={this.handleChange}
                placeholder="Karachi"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-date">Date of Birth</Label>
              <Input
                type="date"
                id="customer-dob"
                name="dob"
                defaultvalue={this.state.activeItem.value}
                onChange={this.handleChange}
                placeholder="07/12/1999"
              />
            </FormGroup>
            <FormGroup>
              <Label for="customer-review">Reviews</Label>
              <Input
                type="text"
                id="customer-review"
                name="review"
                defaultvalue={this.state.activeItem.value}
                onChange={this.handleChange}
                placeholder="Say Something!"
              />
            </FormGroup>
            {/* <FormGroup check>
              <Label check>
                <Input
                  type="checkbox"
                  name="completed"
                  checked={this.state.activeItem.completed}
                  onChange={this.handleChange}
                />
                Completed
              </Label>
            </FormGroup> */}
          </Form>
        </ModalBody>

        
        
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}