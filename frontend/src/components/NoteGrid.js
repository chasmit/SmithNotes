import React, { useState, useEffect } from 'react';
import { Col, Container, Row } from "reactstrap";

import axios from 'axios';

import NotePreview from "./NotePreview";

import { BACK_ENDPOINT } from "../config.js"

import "../App.css";

function NoteGrid() {
    const [notes, setNotes] = useState([]);
    const [isLoading, setLoading] = useState(true);

    useEffect(() => {
        async function getNotes() {
          axios.get(`${BACK_ENDPOINT}`).then((response => {
            setNotes(response.data);
            setLoading(false);
          }));
        }
        getNotes();
      }, []);
      

    return (
        <div className="app-main">
        <Container className="grid">
            {(!isLoading && notes.length > 0) ? (
                <Row className="grid-row">
                {notes.map((note) => {
                    return (
                        <Col sm={3} className="grid-col">
                            <NotePreview note={note} key={note.id}/>
                        </Col>
                    )
                })}
                </Row>
            ) : (
                    <div>No notes have been added yet</div>
                )
            }
        </Container>
        </div>
    )
}

export default NoteGrid;