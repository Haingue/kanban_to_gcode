use std::{fs::{self}, env::{self, Args}, io::Read};
use roxmltree::Document;
use svg2gcode::{svg2program, ConversionConfig, ConversionOptions, Machine};
use g_code::emit::{format_gcode_fmt, FormatOptions};

fn main() {
    let mut args: Args = env::args();

    /* Read & Parse SVG */
    let svg_file: String;
    if args.len() > 1 {
        let parameter: String = args.nth(1)
            .expect("Should be a parameter name");
        if parameter.eq("--input") {
            dbg!("[Svg_To_Gcode] Input mode");
            svg_file = args.nth(2)
                .expect("Should be in arguments");
        } else if parameter.eq("--stream") {
            dbg!("[Svg_To_Gcode] Stream mode");
            let mut buffer:String = String::new();
            std::io::stdin().read_to_string(&mut buffer)
                .expect("The stdin should be filled by XML content");
            svg_file = buffer.clone();
        } else if parameter.eq("--test") {
            dbg!("[Svg_To_Gcode] Test mode");
            let svg_path: &str = "../kanban_to_svg/resources/test.svg";
            svg_file = fs::read_to_string(svg_path)
                .expect("Should have been able to read the file");
        } else {
            panic!("the parameters are not valid")
        }
    } else {
        panic!("Missing parameters, try --input <xml content> or --stream or --test")
    }
    let doc: Document<'_> = Document::parse(&svg_file)
            .expect("Error during the parsing of the String document as XML document");

    /* Configure */
    let conf: ConversionConfig = ConversionConfig::default();
    let options: ConversionOptions = ConversionOptions {
        dimensions: [None; 2]
    };
    let machine: Machine<'_> = Machine::default();

    /* Convert to Gcode */
    let program: Vec<g_code::emit::Token<'_>> = svg2program(&doc,
        &conf,
        options,
        machine);
    let mut gcode:String = String::new();
    format_gcode_fmt(&program, FormatOptions::default(), &mut gcode)
        .expect("Should be able to convert xml(svg) to gcode");

    println!("{}", gcode)
}