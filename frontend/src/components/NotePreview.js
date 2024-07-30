import React from 'react';
import { Link } from "react-router-dom";
import { Card, CardBody, CardText, CardTitle } from "reactstrap";

function NotePreview({note}) {

    return (
        <Card className='note-preview'>
            <CardBody>
                <CardTitle tag="h5">{note.header}</CardTitle>
                <CardText tag="h6">{note.body}</CardText>
                <Link className="app-button" to={{pathname: `/form/${note.id}`}}>
                    View Note
                </Link>
            </CardBody>
        </Card>
    );
}

export default NotePreview;