getqr
=====

Web-based [QR code](http://en.wikipedia.org/wiki/QR_code) generator.
It is [Google Chart Tool](https://developers.google.com/chart/infographics/docs/qr_codes)'s replacement.

Syntax
------

Root URL: `http://getqr.herokuapp.com/qr`

<table cellspacing="code" cellpadding="1">
<tr>
  <th scope="col">Parameter</th>
  <th scope="col">Required or Optional</th>
  <th scope="col">Description</th>
</tr>
<tr>
  <td><code>chs=&lt;<em>width</em>&gt;x&lt;<em>height</em>&gt;</code></td>
  <td><strong>Required</strong></td>
  <td> Image size.</td>
</tr>
<tr>
  <td><code>chl=&lt;<em>data</em>&gt;</code></td>
  <td><strong>Required</strong></td>
  <td>The data to encode. Data can be digits (0-9), alphanumeric characters,
      binary bytes of data, or Kanji. You cannot
      mix data types within a QR code. The data must be UTF-8 URL-encoded. Note
      that URLs have a 2K maximum length, so if you want to encode more than
      2K bytes (minus the other URL characters), you will have to send your data
      using POST.
  </td>
</tr>
<tr>
  <td><code>chld=&lt;<em>error_correction_level</em>&gt;|&lt;<em>margin</em>&gt;</code></td>
  <td>Optional</td>
  <td>
   <ul>
       <li><em>error_correction_level</em> - QR codes support four levels of
          error correction to enable recovery of missing, misread, or obscured
          data. Greater redundancy is achieved at the cost of being able to store
          less data. Here are the supported values:
       <ul>
           <li><code>L</code> - [<em>Default</em>] Allows recovery of up to
                7% data loss</li>
           <li><code>M</code> - Allows recovery of up to 15% data loss</li>
           <li><code>Q</code> - Allows recovery of up to 25% data loss</li>
           <li><code>H</code> - Allows recovery of up to 30% data loss</li>
       </ul>
       </li>
       <li><em>margin</em> - The width of the white border around the data portion
          of the code. This is in <em>rows</em>, not in <em>pixels</em>. The default value is
          4.
       </li>
   </ul>
  </td>
</tr>
</table>


Example
-------

![Example](http://getqr.herokuapp.com/qr?chl=test&chs=200x200)
