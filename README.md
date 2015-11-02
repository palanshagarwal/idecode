# idecode
#### Web Link:  http://idecode.herokuapp.com/

- This is the code repo for a online code compiler. It uses Hackerearth APIs.  
- The editor is an open source editor named ACE ( https://ace.c9.io/#nav=about )  
tweaked a little to fill requirements.  
- Features supported by this version includes:
    - Setting a filename for your code.  
    - Selecting a language according to which your code should run.  
    - After compile & run atleast once, unique links are generated for the code:  
        - Read Only link : Anyone having this link can view the code, compile it in any language, see the output,but can't change it's filename and source code.
        - Read & Write Link: Anyone having this link can in addition to previous, edit the filename and source code too.  
    - Users can give custom inputs for their code prior to compiling.  
    - An existing code can be cloned. The cloned code again has unique links ready to be shared.
    - Any code compiled & shared atleast once can be downloaded as a file directly.
    
- To ensure read only and read & write access to a code, a unique hashed key is generated, the first time a code is compiled & run.
- The system also keeps track of the no. of times a code is compiled & run, represented by Run Count.  
To prevent this increment going into race condition, Django F expressions are used for atomic update.
