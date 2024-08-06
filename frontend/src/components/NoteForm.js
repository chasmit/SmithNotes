import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { Button, Form, FormGroup, Input } from "reactstrap";

import axios from "axios";

import { BACK_ENDPOINT } from "../config.js";

function NoteForm(writeNote = () => {} ) {
    const { id } = useParams();
    const navigate = useNavigate();

    const [header, setHeader] = useState("");
    const [body, setBody] = useState("");
    const [image, setImage] = useState(null);

    useEffect(() => {
        console.log(id);
        async function getData() { 
            if (id) {
                axios.get(`${BACK_ENDPOINT}/${parseInt(id)}/`).then((form) => {
                    setHeader(form.data.header);
                    setBody(form.data.body);
                    setImage(form.data.image);
                }).catch((e) => {
                    console.log(e);
                });
            }
            else {
                setHeader("");
                setBody("");
                setImage("");
            }
        }
        getData();
    }, [id]);


    const handleSubmit = async(e) => {
        e.preventDefault();

        const formData = new FormData();
        if (id) {
            formData.append('id', id);
        }
        formData.append('header', header);
        formData.append('body', body);
        formData.append('image', image);

        console.log(formData);
    
        try {
            let response;
            //note exists: being modified
            if (id) {
                response = await axios.patch(`${BACK_ENDPOINT}/${id}/modify/`, formData);
                writeNote((previous) => {
                    previous.map((note) => (note.id === response.data.id ? response.data : note));
                });

                alert("Note modified!");
                navigate.push("/");
            // note does not exist: being created
            } else {
                response = await axios.post(`${BACK_ENDPOINT}/create/`, formData);
                
                writeNote(response.data);
             
                setHeader("");
                setBody("");
                setImage(null);

                alert("Note created!");
                navigate.push("/");
            } 
        } catch (e) {
            console.log(e);
            console.log(formData);
        }
    }

    return (
        <div className="app-main">
            <Form className="form" onSubmit={handleSubmit}>
                <FormGroup>
                    <Input
                        id="header"
                        name="header"
                        className="note-header"
                        value={header}
                        type="textarea"
                        placeholder={header ? header : "Header"}
                        onChange={(e) => setHeader(e.target.value)}
                    />
                </FormGroup>
                <FormGroup>
                    <Input
                        id="body"
                        name="body"
                        className="note-body"
                        value={body}
                        type="textarea"
                        placeholder={body ? body : "Type note here"}
                        onChange={(e) => setBody(e.target.value)}
                    />
                </FormGroup>
                <FormGroup>
                    <Input
                        id="image"
                        name="image"
                        type="file"
                        onChange={(e) => setImage(e.target.files[0])}
                    >
                        Attach Image
                    </Input>
                </FormGroup>
                <FormGroup>
                    <Button className="app-button" type="submit">
                        {id ? "Modify Note" : "Create Note"}
                    </Button>
                </FormGroup>
            </Form>
        </div>
    );
}

export default NoteForm;